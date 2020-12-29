from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if(log=="critical"):
        app.logger.critical("critical level")
    elif(log=="error"):
        app.logger.error("error level")
    elif(log=="warning"):
        app.logger.warning("warning level")
    else:
        app.logger.info("logging not working")
    return render_template(
        'index.html',
        log=log
    )
