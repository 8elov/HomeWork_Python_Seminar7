import view
import process
import log

def button_click():
    mode = int(view.input_mod())
    if mode == 1: # 1 - импорт из справочника, 2 - экспорт в справочник
        surname = view.input_import()
        res_search = process.search(surname)
        view.view_import(res_search)
        log.log_cash(mode, surname)
    elif mode == 2:
        result = view.input_export()
        process.export(result)
        log.log_cash(mode, result[1::])