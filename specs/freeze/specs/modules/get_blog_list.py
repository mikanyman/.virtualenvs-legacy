def list_blogs():
    """
    Parallel to get_list.py
    Reason for returning empty dictionary is to get RequestContext
    in use for variables like {{ status }}{{ project }}{{ lang }} etc.
    Template: blog/blog_list.html
    """
    return {}