def start_bot():
    from maxdmg_resource    import MaxDmgLoader
    from maxdmg_back        import get_api
    from maxdmg_docgen      import Docgen

    from .bot               import (
        dp, 
        start_polling, 
        start_webhook,
        config,
    )
    from .Factories         import (
        BackAPIFactory, 
        DocumentFactory
    )
    from .Storage           import Storage
    from .Utils             import (
        CommandsManager, 
        DanglingSessionsManager
    )
    from .Statistics        import init_stats_db

    init_stats_db()

    resp = MaxDmgLoader().Load(
        config.AIRTABLE_API_KEY,
        config.AIRTABLE_BASE_ID,
        config.AIRTABLE_STATES_TABLE_ID,
        config.AIRTABLE_STATES_TABLE_VIEW_ID,
        config.AIRTABLE_TRANSITIONS_TABLE_ID,
        config.AIRTABLE_TRANSITION_TABLE_VIEW_ID,
        config.AIRTABLE_FORMS_TABLE_ID,
        config.AIRTABLE_FORMS_TABLE_VIEW_ID,
        config.AIRTABLE_CONFIG_TABLE_ID,
        config.AIRTABLE_CONFIG_TABLE_VIEW_ID,
    )
    back_api    = get_api(resp) 
    docgen      = Docgen(resp['docs'], config)

    DocumentFactory.INIT(docgen)

    BackAPIFactory.INIT(back_api)
    back_info = back_api.RegisterFrontendAPI(None)
    Storage().SetBackInfo(back_info)

    CommandsManager.SetCommands()

    import app.middleware
    middleware.setup(dp)

    import app.handlers
    
    if config.WEBHOOK:
        start_webhook(config)
    else:
        start_polling(config)

