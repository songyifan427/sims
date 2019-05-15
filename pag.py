from flask import request
import math
def pages(counts,pageNum):
    #couunts总条数，pageNum每页条数
    if request.url.find("?")<0:
        url=request.url+"?page="
    else:
        if request.url.find("page")<0:
            url=request.url+"&page="
        else:
            url=request.url[0:request.url.rfind("=")+1]
    pageCounts=math.ceil(counts/pageNum)
    currentPage=int(request.args.get("page") or 0)
    strs="共%s页" %(pageCounts)
    strs+=" <a href='%s'>首页</a> "%(url+str(0))
    last=currentPage-1 if currentPage-1>0 else 0
    strs+=" <a href='%s'>上一页</a> "%(url+str(last))
    start=currentPage-2 if currentPage-2> 0 else 0
    end=start+4 if currentPage+4<pageCounts else pageCounts
    for item in range(start,end):
        if currentPage==item:
            strs+=" <a href='%s' style='color=red'>%s</a> "%(url+str(item),item+1)
        else:
            strs+=" <a href='%s'>%s</a> "%(url+str(item),item+1)
    next=currentPage+1 if currentPage+1<pageCounts else pageCounts-1
    strs+=" <a href='%s'>下一页</a> "%(url+str(next))
    strs+=" <a href='%s'>尾页</a> "%(url+str(pageCounts-1))
    limit=" limit "+str(currentPage*pageNum)+","+str(pageNum)
    return {'limit':limit,'strs':strs}