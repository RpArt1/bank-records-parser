
from tools.utlis import get_project_root

class BankEnum():
    project_root_path = get_project_root()
    MBANK = str(project_root_path) + "/tools/upload/prepare_mbank_file.sh"

    def get_bank_enum_by_name (self, bank_name) :
    
        """ Description
        :type self:
        :param self:
    
        :type bank_name: String 
        :param bank_name: name of bank
    
        :raises:
    
        :rtype: full path of formatting script
        """    
        if (bank_name == "MBANK"):
            return BankEnum.MBANK
    