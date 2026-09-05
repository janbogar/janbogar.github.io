import re
from pathlib import Path

pattern = re.escape("""< a href="javascript:toggle('{% capture id %} """) +\
        r'\d*'+\
        re.escape(''' {%endcapture%}{{id}}');"> <img src="{{ site.baseurl }}/images/add.svg" class="inlinedisplayimg" id="{{id}}_displayimg" /> <img src="{{ site.baseurl }}/images/minus.svg" class="inlinehideimg" id="{{id}}_hideimg" />  \\[{{id}}\\] </a> <span id="{{id}}" class="collapsible" > ''') +\
         r"(.*?)"+re.escape(r"</span>")
pattern=pattern.replace("\\ ",r"\s*")
pattern=re.compile(pattern)

replacement=r"""{% include collapsible.html content= "\1"%}"""

for path in Path(".").glob("**/*.md"):
    with open(path) as f:
        original=f.read()
    new=pattern.sub(replacement,original)
    if not original==new:
        print(path)
    with open(path,"w") as f:
        f.write(new)