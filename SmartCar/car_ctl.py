class Car:
    def set_leftv(self, v):
        pass

    def set_rightv(self, v):
        pass

    def go_straitht(self, v):
        self.set_leftv(v)
        self.set_rightv(v)

    def roate(self,v,r,dir):
        if r == 0 and dir == 1:
            self.set_rightv(v)
            self.set_leftv(-v)
        elif r == 0 and dir !=1:
            self.set_leftv(v)
            self.set_rightv(-v)
        elif r!=0 and dir ==1:
            pass
        else:
            pass

