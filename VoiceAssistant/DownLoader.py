import wget

print('Beginning file download with wget module')

url = 'https://ru.traveltables.com/img/flags_gifs/blr.gif'
# wget.download(url, 'C:/intel/Downloads/blr.gif')
# wget ftp://URL/PATH_TO_FTP_DIRECTORY/*
# ftp://URL/PATH_TO_FTP_DIRECTORY/*
wget.download(url, 'Downloads/')