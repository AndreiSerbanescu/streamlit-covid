import os
from common import utils
from common.utils import *
import subprocess as sb
import shutil

def covid_detector_base(source_file, model_path, get_volumes_from_output_directory, output_dir):

    data_share = os.environ["DATA_SHARE_PATH"]
    script_path = "/app/code/keras_retinanet/bin/evaluate.py"

    input_path, label_path, cp_exit_code = __create_and_copy_files_to_tmp_input_directory(source_file)

    if cp_exit_code == 1:
        return {}, False


    tmp_output_path = __create_shared_output_directory()


    # get real output dir
    # this is a hack
    final_output = os.path.split(source_file)[0]

    assert os.path.split(final_output)[1] == "input"
    final_output = os.path.split(final_output)[0]
    final_output = os.path.join(final_output, "output")

    mv_all_output = f"mv {tmp_output_path}/* {final_output}/"
    print("calling", mv_all_output)



    preproc_path = os.path.join(tmp_output_path, "preprocessed")
    os.mkdir(preproc_path)

    # overwrite model path
    model_path = "/app/model/vgg19_nl_csv_16.h5"

    preprocess_cmd = f"cd /app/code && python3 /app/code/keras_retinanet/bin/pre_process.py --data-source={input_path} --label-source={label_path} --save-path={preproc_path}"

    fst_inf_cmd = f"cd /app/code && python3 /app/code/keras_retinanet/bin/evaluate.py --model={model_path} --gpu=0 --save-path={tmp_output_path} --annotations={preproc_path}/h5_normalize/all_annotations_h5_whole_vol.csv --score-threshold=0.4 --get_predicted_bbox --save-result"

    snd_inf_cmd = f"cd /app/code && python3 /app/code/keras_retinanet/bin/evaluate.py --model={model_path} --gpu=0 --save-path={tmp_output_path} --annotations={preproc_path}/h5_normalize/all_annotations_h5_whole_vol.csv --score-threshold=0.4"


    log_debug("Running", preprocess_cmd)
    exit_code = sb.call([preprocess_cmd], shell=True)
    if exit_code == 1:
        return {}, False

    log_debug("Running", fst_inf_cmd)
    exit_code = sb.call([fst_inf_cmd], shell=True)
    if exit_code == 1:
        return {}, False

    log_debug("Running", snd_inf_cmd)
    exit_code = sb.call([snd_inf_cmd], shell=True)

    if exit_code == 1:
        return {}, False
    shutil.rmtree(input_path)

    # get names of files
    # files = os.listdir(tmp_output_path)

    mv_all_output = f"mv {tmp_output_path}/* {final_output}/"
    print("calling", mv_all_output)

    sb.call([mv_all_output], shell=True)


    return {}, True


    # print(files)
    # assert len(files) == 2

    # mask_volume, detection_volume = get_volumes_from_output_directory(files)
    #
    # print(mask_volume, detection_volume)
    # if mask_volume == "" or detection_volume == "":
    #     return {}, False
    #
    # rel_mask_volume_path = os.path.join(output_dir, mask_volume)
    # rel_detection_volume_path = os.path.join(output_dir, detection_volume)
    #
    # log_debug("rel attention volume", rel_mask_volume_path)
    # log_debug("rel detection volume", rel_detection_volume_path)
    #
    # os.makedirs(os.path.join(data_share, output_dir), exist_ok=True)
    #
    # tmp_mask_path = os.path.join(tmp_output_path, mask_volume)
    # data_share_mask_path = os.path.join(data_share, rel_mask_volume_path)
    # mv_cmd1 = "mv {} {}".format(tmp_mask_path, data_share_mask_path)
    # sb.call([mv_cmd1], shell=True)
    #
    # tmp_volume_path = os.path.join(tmp_output_path, detection_volume)
    # data_share_volume_path = os.path.join(data_share, rel_detection_volume_path)
    # mv_cmd2 = "mv {} {}".format(tmp_volume_path, data_share_volume_path)
    # sb.call([mv_cmd2], shell=True)
    #
    # shutil.rmtree(tmp_output_path)
    #
    # result_dict = {
    #     "auxiliary_volume": rel_mask_volume_path,
    #     "detection_volume": rel_detection_volume_path
    # }
    #
    # return result_dict, True

def __create_and_copy_files_to_tmp_input_directory(source_file):
    tmp = "/tmp"
    input_path_base = os.path.join(tmp, "input-" + utils.get_unique_id())

    if os.path.exists(input_path_base):
        shutil.rmtree(input_path_base)

    os.mkdir(input_path_base)

    input_path = os.path.join(input_path_base, "input")
    label_path = os.path.join(input_path_base, "label")
    os.mkdir(input_path)
    os.mkdir(label_path)

    cp_cmd = "cp {} {}".format(source_file, input_path)

    label_source_file = source_file[:len(source_file) - 7]
    label_source_file = label_source_file + "_lung.nii.gz"

    cp_label_cmd = f"cp {label_source_file} {label_path}"

    log_debug("Running", cp_cmd)
    cp_exit_code = sb.call([cp_cmd], shell=True)

    log_debug("Running", cp_label_cmd)
    sb.call([cp_label_cmd], shell=True)
    return input_path, label_path, cp_exit_code

def __create_shared_output_directory():

    tmp_output_path = "/tmp/output-" + utils.get_unique_id()
    if os.path.exists(tmp_output_path):
        shutil.rmtree(tmp_output_path)

    os.mkdir(tmp_output_path)

    return tmp_output_path
