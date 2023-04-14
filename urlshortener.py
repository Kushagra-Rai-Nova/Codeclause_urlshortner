import requests 
def shorten_url(full_url,link_name):
    API_KEY ='3ee0310bc59cad91884bd91f139c681b71b62'
    BASE_URL ='https://cutt.ly/api/api.php'
    
    payload={'key':API_KEY,'short':full_url,'name':link_name}  
    request=requests.get(BASE_URL,params=payload)
    data=request.json()
    
    print('') 
    
    try:
        title=data['url']['title']
        short_link=data['url']['shortLink'] 
        
        print('Title:',title)
        print('Short Link:',short_link) 
    except:
        status=data['url']['status']
        print('Error:',status)
        
link_name=input('Enter the link:  ')
name=input('give a name to your link:  ')

shorten_url(link_name,name) 