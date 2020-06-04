from common.utils import *
from common import listener_server
import os
from lesion_detector_common.common import *

output_dir = "covid_lesion_detection_output"
output_path = os.path.join(os.environ["DATA_SHARE_PATH"], output_dir)

def __get_attention_and_detection_volumes(files):

    attention_volume = ""
    detection_volume = ""

    for file in files:
        name = os.path.split(file)[1]

        if "attention" in name:
            attention_volume = file
        elif "detection" in name:
            detection_volume = file

    return attention_volume, detection_volume

def covid_detector(param_dict):
    model_path = "/app/model/vgg19_csv_01.h5"
    rel_source_file = param_dict["source_file"][0]
    data_share = os.environ["DATA_SHARE_PATH"]

    # remove trailing / at the beggining of name
    # otherwise os.path.join has unwanted behaviour for base dirs
    # i.e. join(/app/data_share, /app/wrongpath) = /app/wrongpath
    rel_source_file = rel_source_file.lstrip('/')

    source_file = os.path.join(data_share, rel_source_file)

    return covid_detector_base(source_file, model_path, __get_attention_and_detection_volumes, output_dir)


def covid_detector_absolute(source_file):
    model_path = "/app/model/vgg19_csv_16.h5"
    return covid_detector_base(source_file, model_path, __get_attention_and_detection_volumes, output_dir)


if __name__ == "__main__":

    setup_logging()
    log_info("Started listening")

    served_requests = {
        "/covid_detector_nifti": covid_detector
    }

    listener_server.start_listening(served_requests, multithreaded=True, mark_as_ready_callback=mark_yourself_ready)

