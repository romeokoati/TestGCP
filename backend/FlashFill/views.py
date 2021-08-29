from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import FlashFill.Algorithmes.UniformQuickFill as UFF




class FlashFillExecutionList(APIView):    
    def get(self, request, format=None):
            print("++++++++++++++++++++++++",request.query_params['TestCountry'])
            datas = {}
            """             filename = 'dataTest2.txt'
                        presentelement = ''
                        Test = UFF.UniformQuickFill()
                        Test.GetClassC()
                        ListeOfProgrammes = list(Test.GenerateStringProgram2(Test.GetExamples()[2]))
                        if len(ListeOfProgrammes) != 0:
                            datas = Test.ExecuteOnElements(filename,ListeOfProgrammes[0])
                        else:
                            datas = "Flash Fill limite" """
                
                
            return Response(datas)


    @classmethod
    def get_extra_actions(cls):
        return []