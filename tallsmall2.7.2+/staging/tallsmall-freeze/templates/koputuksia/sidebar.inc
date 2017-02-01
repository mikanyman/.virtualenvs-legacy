<div id="sidebar">
  <h3 class="sub">Osastot</h3>
  <ul class="sub">
  {% for ord_dict in dict_of_ords_cats_nums.items|dictsort:"0" %}
    {% for cats in ord_dict.1.items %}
      {% ifnotequal cats.1 0 %}
        {% ifequal cats.0 category_name %}
          <li class="active"><a href="/sites/specs/koputuksia/{{ issue_num }}/{{ cats.0 }}/">{{ cats.0 }}</a> <i>({{ cats.1 }})</i></li>
        {% else %}
          <li><a href="/sites/specs/koputuksia/{{ issue_num }}/{{ cats.0 }}/">{{ cats.0 }}</a> <i>({{ cats.1 }})</i></li>
        {% endifequal %}
      {% endifnotequal %}
    {% endfor %}
  {% endfor %}
  {% if not category_name %}
    <li class="active"><a href="/sites/specs/koputuksia/{{ issue_num }}/">Kaikki</a></li>
  {% else %}
    <li><a href="/sites/specs/koputuksia/{{ issue_num }}/">Kaikki</a></li>
  {% endif %}
  </ul>

  <h3 class="sub">Lehden numerot</h3>
  <ul class="sub">
  {% for elems in dict_of_issues_nums.items %}
    {% ifnotequal elems.1 0 %}
      {% ifequal elems.0 issue_num %}
        <li class="active"><a href="/sites/specs/koputuksia/{{ elems.0 }}/">{{ elems.0 }}</a> <i>({{ elems.1 }})</i></li>
      {% else %}
        <li><a href="/sites/specs/koputuksia/{{ elems.0 }}/">{{ elems.0 }}</a> <i>({{ elems.1 }})</i></li>
      {% endifequal %}
    {% endifnotequal %}
  {% endfor %}
  </ul>
</div><!-- end #sidebar -->
