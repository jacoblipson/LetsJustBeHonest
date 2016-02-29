from rest_framework import serializers

from .models import Politician, Statement


class PoliticianSerializer(serializers.ModelSerializer):
    statement_counts = serializers.SerializerMethodField('get_statement_counts')

    @staticmethod
    def statement_counts(obj):
        return {
            'total': obj.statements.count(),
            'true': obj.statements.filter(ruling=Statement.TRUE).count(),
            'mostly_true':
                obj.statements.filter(ruling=Statement.MOSTLY_TRUE).count(),
            'half_true':
                obj.statements.filter(ruling=Statement.HALF_TRUE).count(),
            'mostly_false':
                obj.statements.filter(ruling=Statement.MOSTLY_FALSE).count(),
            'false': obj.statements.filter(ruling=Statement.FALSE).count(),
            'pants_on_fire':
                obj.statements.filter(ruling=Statement.PANTS_ON_FIRE).count()
        }

    class Meta:
        model = Politician
