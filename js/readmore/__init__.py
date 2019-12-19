from __future__ import absolute_import
from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('js.readmore', 'resources')

readmore_js = Resource(
    library,
    'readmore.js',
    minified='readmore.min.js',
    depends=[jquery]
)

readmore = readmore_js
