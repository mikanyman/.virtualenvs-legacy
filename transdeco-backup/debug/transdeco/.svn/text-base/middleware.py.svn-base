from transdeco.counter.models import ViewCount, PathCount

class ViewCountMiddleware(object):
    def process_request(self,request):
        if is_count_path(request.path):
            view_count = ViewCount.objects.filter(url=request.path)
            if view_count:
                view_count[0].count += 1
                view_count[0].save()
            else:
                ViewCount(url=request.path).save()


def is_count_path(path):
    if not path.endswith('/'):
        path = path+'/'
    except_paths = [p.path for p in PathCount.objects.all()]
    for p in except_paths:
        wildcard =  p.endswith('*')
        if wildcard:
            p=p.replace('*', '')

        if p == path:
            return False
        #wildcard?
        if wildcard:
            if path.startswith(p):
                return False
    return True
