import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from .models import *


class createContact(APIView):
    def post(self,request):
        try:
            serializer = CreateNameSerializer(data=request.data)
            if serializer.is_valid():
                name = serializer.data["name"]
                address = serializer.data["address"]
                phone = serializer.data['phone']
                email = serializer.data["email"]

                contact.objects.create(
                    name = name,
                    address = address,
                    phone = phone,
                    email = email,
                )
                data = {'Message': "You have created New Contact Successfully",
                        "data": serializer.data}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

    def get(self,request):
        try:
            result = list(contact.objects.filter().values())
            return JsonResponse(result, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class getSpecificContact(APIView):
    def get(self,request,id):
        try:
            result = list(contact.objects.filter(id=id).values())
            return JsonResponse(result, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


    def put(self,request,id):
        try:
            serializer = UpdateContactSerializer(data=request.data)
            if serializer.is_valid():
                contact.objects.filter(id=id).update(
                    **serializer.data
                )
                data = {'Message': "You have Updated  Contact Successfully",
                        "data": serializer.data}
                return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)

    def get_object(self, id):
        try:
            return contact.objects.get(id=id)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            result = self.get_object(id)
            result.delete()
            data = {'Message': "You have Deleted Contact Successfully"}
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)



class contactsCallList(APIView):
    def get(self,request):
        try:
            res2=[]
            result = list(contact.objects.filter().values())
            # print(result)

            for var in result:
                # var["name"] = list(eval(var["name"]))
                var["phone"] = list(eval(var["phone"]))
                for var2 in var["phone"]:
                    # print(var2.keys())
                    if var2["type"] == "home":
                        res2.append(var)

            finalR= {}
            for var in res2:
                finalR[var["id"]] = var
            print(finalR)
            dataR = list(finalR.values())
            return JsonResponse(dataR, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse(str(e), safe=False,status=status.HTTP_400_BAD_REQUEST)