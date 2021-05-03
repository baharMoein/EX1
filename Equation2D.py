 def Equation2D (b, d, f):
	a = d*d-4*b*f
	if a == 0 :
	    return (-d/2*b)
	else:
	    if a< 0 :
         return ("no answer")
      else: 
          return ((-d+((d**2-4*b*f)**0.5)/2*b) , (-d-((d**2-4*b*f)**0.5))/2*a)
          
 b = float(input('b=:'))
 d = float(input('d=:'))
 f = float(input('f=:')) 
      		    
 print ("answer(e) ",(equation2D(b,d,f)))
