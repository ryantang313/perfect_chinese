from bpy.props import StringProperty
from bpy.types import Operator

from ..localization import PC_LocalizationManager
from ..types import PC_Registrable
from ..utils import PC_Info
from ..config import PC_Config


class PC_ModuleEnable(Operator, PC_Registrable):
  bl_idname = "perfect_chinese.module_enable"
  bl_label = "注冊模組翻譯"
  bl_options = {'INTERNAL'}

  module: StringProperty(name="模組", description="注冊翻譯的模組名字")

  def execute(self, context):
    PC_LocalizationManager.register_module_and_add_to_list(self.module)
    PC_LocalizationManager.update_global_module_only()
    PC_Config.update_config()
    return {"FINISHED"}


class PC_ModuleDisable(Operator, PC_Registrable):
  bl_idname = "perfect_chinese.module_disable"
  bl_label = "注銷模組翻譯"
  bl_options = {'INTERNAL'}

  module: StringProperty(name="模組", description="注銷翻譯模組的名字")

  def execute(self, context):
    PC_LocalizationManager.unregister_module_and_remove_from_list(self.module)
    PC_Config.update_config()
    return {"FINISHED"}


class PC_ModuleRefresh(Operator, PC_Registrable):
  bl_idname = "perfect_chinese.module_refresh"
  bl_label = "刷新"
  bl_description = "刷新本地模塊列表"
  bl_options = {'INTERNAL'}

  def execute(self, context):
    PC_LocalizationManager.moudle_refresh()
    return {'FINISHED'}


class PC_UpdateGlobalModule(Operator, PC_Registrable):
  bl_idname = "perfect_chinese.update_global_module"
  bl_label = "更新全局翻譯"
  bl_options = {'INTERNAL'}

  def execute(self, context):
    PC_LocalizationManager.update_global_module()
    return {"FINISHED"}
