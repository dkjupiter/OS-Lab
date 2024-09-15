def inputCheck(CowId, CowOld_y, CowOld_m, CowCntUdder):
    isValid = True
    CowOld_y = int(CowOld_y)
    CowOld_m = int(CowOld_m)
    CowCntUdder = int(CowCntUdder)
    
    # cow id len < 8
    if not CowId.isdigit() or len(CowId) > 8 :
        isValid = False
        
    # first cow id != 0
    if CowId[0] == '0':
        isValid = False
    
    # Old cow validation
    if int(CowOld_y) > 10 or int(CowOld_m) > 12 or (int(CowOld_y) == 10 and int(CowOld_m) > 0):
        isValid = False
            
    # count udder cow
    if not isinstance(CowCntUdder, int) or (CowCntUdder != 3 and CowCntUdder != 4) or CowOld_m == None:
        isValid = False
              
    return isValid


        