from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from Affine.Cryp_affine import getKeyParts, checkKeys, encryptMessage, decryptMessage
from AffineHack import hackAffine
from django.core.context_processors import csrf
# Create your views here.

def home(request):
	c = {}
	c.update(csrf(request))
	return render(request,'home.html',c)

def trigger(request):

	if request.method == 'POST':

		m1 = request.POST.get('m1','')
		m2 = request.POST.get('m2','')
		mode = request.POST.get('mode','')
		key = int(request.POST.get('key'))
		#print m1 + m2 + mode + str(key)
		if mode == 'Encrypt':
			cipher = encryptMessage(key, m1).replace(" ","")
			context = {'cipher':cipher, 'mess':m1}
			return render(request,'home.html', context)
		elif mode == 'Decrypt':
			message = decryptMessage(key,m1)
			context = {'message':message, 'ciph':m1}
			return render(request,'home.html',context)
		else: 
			return render(request,'home.html',{})

def brute(request):
	if request.method == 'POST':
		b_cipher = request.POST.get('b_cipher','')
		plain = hackAffine(b_cipher)
		context = {'plain': plain}
		return render(request,'hack.html',context)






			
		
	