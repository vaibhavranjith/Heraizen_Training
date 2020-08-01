class department:
    def __init__(self,deptno,dname,location):
        self.deptno=deptno
        self.dname=dname
        self.location=location
        self.emplst=[]
    def get_location(self):
        return self.location

    def get_dname(self):
        return self.dname

    def get_deptno(self):
        return self.deptno
    
class employee:
    def __init__(self,empno,ename,job,mgr,hiredate,sal,comm,deptno):
        self.empno=empno
        self.ename=ename
        self.job=job
        self.mgr=mgr
        self.hiredate=hiredate
        self.sal=sal
        self.comm=comm
        self.deptno=deptno

