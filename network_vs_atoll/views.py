from django.shortcuts import render


def home(request):
    diffs = {
        'summary': [
            {
                'technology': 'GSM',
                'count': 356,
            },
            {
                'technology': 'WCDMA',
                'count': 567,
            },
        ],
        'GSM': {
            'summary': [
                {
                    'bsc_name': 'BSC1',
                    'count': 45,
                },
                {
                    'bsc_name': 'BSC2',
                    'count': 34,
                }
            ],
            'BSC1': [],
            'BSC2': [],
        },
        'WCDMA': {
            'summary': [
                {
                    'rnc_name': 'RNC1',
                    'count': 55,
                },
                {
                    'rnc_name': 'RNC2',
                    'count': 77,
                },
            ],
        },
    }
    return render(request, 'network_vs_atoll/home.html', diffs)