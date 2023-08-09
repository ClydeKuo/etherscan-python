from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules


class Log:
    @staticmethod
    def get_log(params: str) -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.LOG}"
            f"{fields.ACTION}"
            f"{actions.GET_LOG}"
            f"{params}"
        )
        return url