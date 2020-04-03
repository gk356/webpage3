def cal_bmi(ht, wgt):
    height_m = ht*0.025
    height_m = round(height_m,2)

    weight_inkg = wgt*0.45
    weight_inkg = round(weight_inkg,2)

    results = weight_inkg/(height_m*height_m)
    results = round(results,2)
    #print(results)
    #results = round(results,1)
    return results
    