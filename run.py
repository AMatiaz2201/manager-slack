URL_DO_SEU_WEBHOOK = 'https://hooks.slack.com/services/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'

from manager_slack import Slack
Slack = Slack(url=URL_DO_SEU_WEBHOOK)


def usa_slack():
    Slack.send_success(mensagem='Deu certo minha integração com slack')

    Slack.send_error(mensagem='Minha mensagem de erro')

    dados = {
        'urlWebHook' : 'https://api.slack.com/messaging/webhooks',
        'imagemSlack' : 'https://user-images.githubusercontent.com/819186/51553744-4130b580-1e7c-11e9-889e-486937b69475.png',
        'nome': 'icone slack'
    }

    Slack.send(mensagem='Segue algumas informações sobre WebHook', dados=dados)

if __name__ == '__main__':
    usa_slack()