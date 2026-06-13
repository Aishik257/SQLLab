from django.views import View
from django.shortcuts import render
from .services.csv_service import CSVService
from .services.sql_service import SQLService
from .services.sample_data_service import SampleDataService


class HomeView(View):

    template_name = "playground/home.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "tables": SQLService.get_tables(),
                "schema": SQLService.get_schema(),
            }
        )

    def post(self, request):

        result = None
        error = None

        action = request.POST.get("action")

        if action == "upload":

            csv_files = request.FILES.getlist("csv_files")

            for csv_file in csv_files:
                CSVService.upload_csv(csv_file)

        elif action == "load_sample":

            SampleDataService.load_sample_data()

        elif action == "query":

            query = request.POST.get("query")

            try:
                response = SQLService.execute_query(query)

                if response["type"] == "table":

                    result = response["data"].to_html(
                        classes="table",
                        index=False
                    )

                else:

                    result = response["data"]

            except Exception as e:
                error = str(e)

        elif action == "delete":

            table_name = request.POST.get("table_name")

            SQLService.delete_table(table_name)

        return render(
            request,
            self.template_name,
            {
                "tables": SQLService.get_tables(),
                "schema": SQLService.get_schema(),
                "result": result,
                "error": error,
                "query": request.POST.get("query", "")
            }
        )
    
class LandingView(View):
    template_name = "landing/landing.html"

    def get(self, request):
        return render(request, self.template_name)