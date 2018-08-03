from qiniu import Auth, put_file, etag
import sys
print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv[0]))
for arg in sys.argv:
    print(arg)

import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = 'hHJLSVlqJ3imbKsKTgS0b969ujbjaQmtjnA8bpH-'
secret_key = 'nKpu1zGEq_5o0zJx7sFjqsLJUL23YrXP_raFwWe6'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'test'
#上传到七牛后保存的文件名
key = 'abczone.txt'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = './abczone.txt'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)



