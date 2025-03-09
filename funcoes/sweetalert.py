import sweetify


def mensagem(request, msg, tipo, categoria):
    match tipo:
        case 'success':
            if categoria == 'toast':
                sweetify.toast(request, msg, icon=tipo, timer=4000)
            else:
                sweetify.success(request, msg, icon=tipo, button='Ok', timer=4000)
        case 'error':
            if categoria == 'toast':
                sweetify.toast(request, msg, icon=tipo, timer=4000)
            else:
                sweetify.error(request, msg, icon=tipo, button='Ok', timer=4000)
        case 'info':
            if categoria == 'toast':
                sweetify.toast(request, msg, icon=tipo, timer=4000)
            else:
                sweetify.info(request, msg, icon=tipo, button='Ok', timer=4000)
        case 'warning':
            if categoria == 'toast':
                sweetify.toast(request, msg, icon=tipo, timer=4000)
            else:
                sweetify.warning(request, msg, icon=tipo, button='Ok', timer=4000)
        case _:
            sweetify.toast(request, msg, icon=tipo, timer=4000)