from .models import Benh, TrieuChung, GiaTri
import numpy as np

def cbr(problem):
    list_benh = Benh.objects.all()
    result = 0
    index = 0
    problem = np.array(problem)

    for case in list_benh:
        list_tc = TrieuChung.objects.all().order_by("ki_hieu");
        list_ts = [];
        list_gt = [];
        for tc in list_tc:
            list_ts.append(GiaTri.objects.get(benh_id = case.id, tc_id = tc.id).trongso)
            list_gt.append(GiaTri.objects.get(benh_id = case.id, tc_id = tc.id).gia_tri)
        list_ts = np.array(list_ts)
        list_gt = np.array(list_gt)
        kq = (list_ts*(1 / (10*(np.abs(problem - list_gt))+1))).sum()/ list_ts.sum()
        if kq > result:
            result= kq
            index = case.id
            print(kq)
    return index



