from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .smart_nodes import PromptRelaySmartEncode, PromptRelaySmartEncodeTest

NODE_CLASS_MAPPINGS["PromptRelaySmartEncode"] = PromptRelaySmartEncode
NODE_CLASS_MAPPINGS["PromptRelaySmartEncodeTest"] = PromptRelaySmartEncodeTest

NODE_DISPLAY_NAME_MAPPINGS["PromptRelaySmartEncode"] = "Prompt Relay Encode (Smart)"
NODE_DISPLAY_NAME_MAPPINGS["PromptRelaySmartEncodeTest"] = "Prompt Relay Smart Encode Test"

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
