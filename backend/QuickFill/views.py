from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import QuickFill.Algorithmes.InteractQuickFill as IFF




class QuickFillExecutionList(APIView):    
    def get(self, request, format=None):
            print("++++++++++++++++++++++++",request.query_params['TestCountry'])
            datas = {}
            Test = IFF.InteractQuickFill()
            Test.GetClassC()
            """ s = Test.GetInteractData()
            print(s[0]) """
            #print(len(Test.GenerateStringProgram(Test.GetInteractData()[0])))
            programme = list(Test.GenerateStringProgram(Test.GetInteractData()[0]))[0]
            #print(programme)
            print(Test.ExecuteFonction(programme,{"b1***F":"aaaFokou34", "b2***V":"aaaVanessa9", "b3***L":"aaaLaure77"},{"v1": "Fokou Vanessa Laure"}))
            
            
            return Response(datas)


    @classmethod
    def get_extra_actions(cls):
        return []