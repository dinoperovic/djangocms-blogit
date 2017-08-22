#!/bin/sh
[ -e "fixtures/example.json" ] && rm fixtures/example.json

./manage.py dumpdata \
    --indent=2 \
    --natural-foreign \
    auth.user \
    cms \
    djangocms_text_ckeditor \
    filer \
    --exclude filer.clipboard \
    --exclude filer.clipboarditem \
    > fixtures/example.json
