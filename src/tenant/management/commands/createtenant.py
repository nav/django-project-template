from django.db import transaction
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from tenant.models import Tenant


class Command(BaseCommand):
    help = "Create a new Tenant"

    def add_arguments(self, parser):
        parser.add_argument("--name", type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        site = Site.objects.create(
            domain=options["domain"],
            name=options["name"],
        )
        tenant = Tenant.objects.create(site=site)
        self.stdout.write(
            self.style.SUCCESS(
                "Tenant created successfully: {}".format(tenant.site.domain)
            )
        )
