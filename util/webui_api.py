from webuiapi import webuiapi

api = webuiapi.WebUIApi()


def generate_sd_grid_control_net(img, prompt="string", negative_prompt="string"):
    unit1 = webuiapi.ControlNetUnit(
        input_image=img,
        module='canny',
        model='control_v11p_sd15_canny [d14c016b]',
        processor_res=img.height if img.height > img.width else img.width
    )
    r = api.txt2img(
        prompt=prompt,
        negative_prompt=negative_prompt,
        controlnet_units=[unit1],
        width=img.width,
        height=img.height,
        steps=50,
        sampler_name='DPM++ 2M Karras',
        cfg_scale=7,
    )
    return r.image


def generate_sd_control_net_img_2_img(img, prompt="string", negative_prompt="string", width=None, height=None):
    unit1 = webuiapi.ControlNetUnit(
        input_image=img,
        module='canny',
        model='control_v11p_sd15_canny [d14c016b]',
        processor_res=img.height if img.height > img.width else img.width
    )
    r = api.img2img(
        images=[img],
        prompt=prompt,
        negative_prompt=negative_prompt,
        controlnet_units=[unit1],
        width=width if width else img.width,
        height=height if height else img.height,
        steps=50,
        sampler_name='DPM++ 2M Karras',
        cfg_scale=7,
    )
    return r.image
