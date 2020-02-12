# -*- coding: utf-8 -*-
from django.http.response import StreamingHttpResponse
from myAPI.fileAPI import file_iterator

def downLoadFile(tempFilePath,downFilePath):
    response = StreamingHttpResponse(file_iterator(tempFilePath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(downFilePath)
    return response
