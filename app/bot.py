from aiogram    import (
    Bot, 
    Dispatcher, 
    types, 
    executor,
)
from .Config    import config


bot = Bot( token=config.API_TOKEN)
dp  = Dispatcher(bot)


def start_polling(config):
    from .Utils import DanglingSessionsManager
    loop = DanglingSessionsManager.Start()
    executor.start_polling(dp, skip_updates=True)


def start_webhook(config):
    from aiohttp import web
    import ssl
    from aiogram.dispatcher.webhook import get_new_configured_app

    app = get_new_configured_app(dispatcher=dp, path=config.WEBHOOK_PATH)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(config.WEBHOOK_SSL_CERT_PATH, 
                            config.WEBHOOK_SSL_PRIV_PATH)

    web.run_app(app, host=config.WEBAPP_HOST, 
                port=config.WEBAPP_PORT, 
                ssl_context=context)
    """
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )
    """

async def on_startup(dp):
    from .Utils  import DanglingSessionsManager

    loop = DanglingSessionsManager.Start()
    await bot.set_webhook(config.WEBHOOK_URL, 
                          certificate=open(config.WEBHOOK_SSL_CERT_PATH, 'rb'),
                          drop_pending_updates=True)

async def on_shutdown(dp):
    await bot.delete_webhook()

