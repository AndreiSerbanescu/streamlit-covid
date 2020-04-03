from lungmask import lungmask

# Loading all models
lungmask.get_model('unet', 'R231')
lungmask.get_model('unet', 'LTRCLobes')
lungmask.get_model('unet', 'R231CovidWeb')
