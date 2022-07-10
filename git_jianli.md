git_jianli

shiyanlou:~/ $ cd Code                                                [9:00:51]
shiyanlou:Code/ $ mkdir CV && cd CV 
hiyanlou:CV/ $ git init                                              [9:02:22]
初始化空的 Git 仓库于 /home/shiyanlou/Code/CV/.git/

shiyanlou:CV/ (master) $ git config --global user.name 'hifuer'       [9:02:59]
shiyanlou:CV/ (master) $ git config --global user.email 'hifuer@qq.com'


shiyanlou:CV/ (master) $ 
shiyanlou:CV/ (master*) $ unzip cv-template.zip 
shiyanlou:CV/ (master*) $ mv cv-template/* .                          #注意 .  命令后的小点 不要忘
shiyanlou:CV/ (master*) $ rm -rf cv-template* __MACOSX*


#去可编辑
$(document).ready(function($){
    $("*").removeAttr('contenteditable');        
})

#部署
$git add .
$git commint -m 'commit my cv'

$git remote add origin 你的远程仓库地址
$git push -u origin master
