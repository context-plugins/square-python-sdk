from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..core import UrlTemplate, param
from .environment import Environment


class ProductionConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://connect.squareup.com"


class SandboxConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://connect.squareupsandbox.com"


class CustomConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "{custom_url}"
    custom_url: str = "https://connect.squareup.com"


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    production: ProductionConfig = Field(default_factory=ProductionConfig)
    sandbox: SandboxConfig = Field(default_factory=SandboxConfig)
    custom: CustomConfig = Field(default_factory=CustomConfig)

    def resolve(self, environment: Environment, path: str) -> UrlTemplate:
        if environment == "production":
            production = self.production
            return UrlTemplate(base_url=production.base_url, path=path)
        if environment == "sandbox":
            sandbox = self.sandbox
            return UrlTemplate(base_url=sandbox.base_url, path=path)
        custom = self.custom
        return UrlTemplate(base_url=custom.base_url, path=path, variables=[param[str]("custom_url", custom.custom_url)])
