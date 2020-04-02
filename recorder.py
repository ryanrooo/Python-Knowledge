import argparse
import json
import os
import shutil
import subprocess

def call_recorder(recorder_path, needs_root_permissions = False):
    cmd = (["sudo"] if needs_root_permissions else []) + [os.path.join(recorder_path, "recorder")]
    subprocess.call(cmd)

def move_recordings(num_recordings, data_dump_path, output_path):
    DW_PREFIX = "dw_"
    VIDEO_NAME = "video_first.raw"
    dw_dir_paths = map(
        lambda e: os.path.join(data_dump_path, e),
        sorted(filter(lambda e: e.startswith(DW_PREFIX), os.listdir(data_dump_path))))

    # A small sanity check
    if len(dw_dir_paths) != num_recordings:
        print "The # of videos recordings doesn't meet with the expected # of recordings..."
        print "Please reset this experiment..."
    else:
        for (recording_num, dw_dir_path) in zip(range(num_recordings), dw_dir_paths):
            shutil.copyfile(
                os.path.join(dw_dir_path, VIDEO_NAME),
                os.path.join(output_path, "video_{}.raw".format(recording_num)))

    for dw_dir_path in dw_dir_paths:
        shutil.rmtree(dw_dir_path)

def record(num_recordings, recorder_path, output_path):
    RECORDER_CONFIG_FILE_NAME = "recorder-config.json"

    # Grab the temporary storage path (i.e. where the recordings are temporarily stored)
    os.chdir(recorder_path)
    current_path = os.getcwd()

    data_dump_path = None
    with open(os.path.join(recorder_path, RECORDER_CONFIG_FILE_NAME), "r") as recorder_config_file:
        recorder_config = json.load(recorder_config_file)
        data_dump_path = os.path.abspath(recorder_config["path"])

    if data_dump_path:
        # Check if output path exists
        if not os.path.isdir(output_path):
            os.makedirs(output_path)

        # Call the recorder app
        call_recorder(recorder_path, True)
        os.chdir(current_path)

        # Move the recordings and clean up
        move_recordings(num_recordings, data_dump_path, output_path)

def main(args):
    (args.recorder_path, args.output_path) = map(
        lambda e: os.path.expanduser(os.path.normpath(e)),
        (args.recorder_path, args.output_path))
    record(args.num_recordings, args.recorder_path, args.output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_recordings", type=int, help="the number of recordings to take")
    parser.add_argument("recorder_path", help="the path to the 'recorder' app")
    parser.add_argument("output_path", help="the path where the recordings will be")

    args = parser.parse_args()
    main(args)

