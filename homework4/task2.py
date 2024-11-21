def extract_query_param(url):

    new_url = url.split('?', 1)[1]

    kew_value_params = new_url.split('&')

    for i in kew_value_params:
        key,value = i.split('=')
        print(f'Key:{key}, Value:{value}')

url = 'http://example.com/products?category=electronics&price=100-500&brand=sony'

extract_query_param(url)
