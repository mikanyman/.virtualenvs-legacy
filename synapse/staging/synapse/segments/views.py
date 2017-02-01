from django.shortcuts import render_to_response, get_object_or_404

def segment_list(request):
    return render_to_response('segments/segment_list.html', {'poll': 'BLA'})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})

