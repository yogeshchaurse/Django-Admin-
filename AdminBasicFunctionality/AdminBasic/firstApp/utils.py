import re
from django.utils.translation import ugettext_lazy


def ugettext_lazy_compact(s):
    """
    Replaces all whitespace with a single space before passing the string
    through for translation.
    """
    #print 's0:',s
    s1 = re.sub(r'[\s\n\t]+', ' ', s).strip()
    #print 's1:',s1
    return ugettext_lazy(s1)

_ = ugettext_lazy_compact
