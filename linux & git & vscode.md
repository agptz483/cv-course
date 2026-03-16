[基于 VScode 的 git 详细使用指南【保姆级！建议收藏！】_vscode使用git-CSDN博客](https://blog.csdn.net/weixin_48024605/article/details/136037857)  

# linux
- 关于Linux的操作和常用指令在之前已经粗略学习过，不过那已经是一年前的事了，现在很笨拙完全记不住快捷键只能一点点手打（bushi  
- 在cv-course中老师要求学生下载wsl并且在其中搭建虚拟环境，一开始我很疑惑，因为一般都是通过conda搭配IDE来实现虚拟环境的管理和项目的分离，但实操之后我发现在wsl中干这事好像更简单一点，而且对于初学者来说与本机windows系统隔离，起码不会把自己的windows搞崩  
- 关于wsl的下载我不写了，因为我的wsl是在一年前下载的，不记得怎么弄了（理直气壮）  
- 以下是cv-course中一些项目创建和虚拟环境搭建步骤：  
```  
mkdir -p ~/cv-course  
cd ~/cv-course  
python3 -m venv .venv-basic  
python3 -m venv .venv-ml  
python3 -m venv .venv-dl  
source .venv-basic/bin/activate  
pip install numpy matplotlib opencv-python  
pip freeze > requirements-basic.txt  
deactivate  
```  
  
# git  
- 这玩意不是很好理解，再一年前我也曾学习git未遂，建议去b站或开头的CSDN网站从头学习一下，然后再实操，实操遇到问题优先问AI（好好问，问清楚），这样慢慢就理解了  
- 推荐最强coder华南理工大学ZJC同学的笔记  
- [whythz.github.io/_posts/2024-08-15-Git入门基础知识汇总.md at main · WhythZ/whythz.github.io](https://github.com/WhythZ/whythz.github.io/blob/main/_posts/2024-08-15-Git%E5%85%A5%E9%97%A8%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E6%B1%87%E6%80%BB.md)  
- 在我看来主要是两个功能：版本管理与远程传输  
	- 版本管理：记录项目文件的修改历史，便于比较和回退版本，防止一不小心改崩代码没招  
	- 远程传输：将项目文件在各种仓库传输，并且实现协作者之间的独立工作与合并文件的有序性，只能说很有用啊。但是这个涉及到SSH密钥的配置，按CSDN教程的做一遍就行  
- 不过如果实在搞不定git，也不是不行，版本管理方面，你可以备份很多文件，然后每一次该代码都产生新文件，根据真实经历这虽然能干下去但会堆出很多屎；远程传输方面，传github上倒是还好，可以直接拖动上去，但是如果你有协作者，那就只能互相发屎的压缩包了  
- 所以git还是很重要的  
  
# git & vscode  
- 如果你害怕在git的bash黑框框里输命令，觉得很麻烦，那么可以在vscode配置git插件，可以非常方便的实现图形化操作，具体的步骤在CSDN教程里讲的很详细，我就分享几个我遇到的问题提供大家参考：  
##### 1、.SSH文件夹  
 - 如果按教程或者正常来弄，配置好SSH密钥后.ssh文件夹会装到windows系统的`C:\Users\ptz\.ssh`路径，可以直接将其复制到wsl里你的项目路径` /\\wsl.localhost\Ubuntu-22.04\home\ptz\.ssh`（不出意外的话文件资源管理器里，此电脑下面应该会有一个小企鹅linux，直接复制过去）  
- 然后按以下步骤设置wsl里.ssh的权限：  
```  
chmod 700 ~/.ssh  
chmod 600 ~/.ssh/id_rsa  
chmod 644 ~/.ssh/id_rsa.pub  
chmod 600 ~/.ssh/id_ed25519 2>/dev/null  # 如果有这个文件  
chmod 644 ~/.ssh/id_ed25519.pub 2>/dev/null  # 如果有这个文件  
chmod 644 ~/.ssh/known_hosts 2>/dev/null  
  
ssh -T git@github.com #测试连接  
```  
##### 2、拉取与推送  
- 有一次我在github网页上编辑了README.md，然后在vscode里直接改了代码，想推送上github的时候发生冲突，原因是两边都有新提交，Git不知道要保留哪个  
- 这时候要先合并，统一项目的版本,或者说先拉取pull，就是把github上的修改拉到本地  
```  
git pull cv-course main --no-rebase --allow-unrelated-histories  
```  
- 这时候我弹出了一个nano 编辑器界面  
```  
GNU nano 6.2 /home/ptz/cv-course/.git/MERGE_MSG   
* Merge branch 'main' of github.com:agptz483/cv-course # Please enter a commit message to explain why this merge is necessary, # especially if it merges an updated upstream into a topic branch. # # Lines starting with '#' will be ignored, and an empty message aborts # the commit. ^G Help ^O Write Out ^W Where Is ^K Cut ^T Execute ^C Location M-U Undo M-A Set Mark M-] To Bracket ^X Exit ^R Read File ^\ Replace ^U Paste ^J Justify ^/ Go To Line M-E Redo M-6 Copy ^Q Where Was  
```  
- 直接按：`Ctrl + X`（退出）  
- 再推送push把本地的修改上传到github  
- 为了避免这种问题，最好养成好习惯，在**本地编辑之前先拉取一下**（当然保证你github仓库上的东西没毛，不然拉错的东西下来干嘛）  