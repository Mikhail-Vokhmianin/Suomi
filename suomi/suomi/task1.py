""" A list of functions for the first task """

def greets(your_name='stranger'):
    """ Greets you in a finnish style
    
    Parameters
    ----------
    your_name: string
    
    Return
    ---------
    Good mood
    """
    
    from datetime import datetime
    import random
    
    hello_list = ["Terve, ",
                  "Hei, ",
                  "Moi, ",
                  "Moika, "]
    
    now = datetime.now().hour+datetime.now().hour/60
    
    if now<=6:
        extra_greet = "Hyvää yötä, "
    elif now<=12:
        extra_greet = "Huomenta, "
    elif now<=18:
        extra_greet = "Hyvää päivä, "
    else:
        extra_greet = "Hyvää iltaa, "
    
    hello_list.append(extra_greet)
    
    print(hello_list[random.randint(0,4)]+your_name+'!')