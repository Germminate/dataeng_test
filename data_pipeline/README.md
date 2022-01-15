# Data Pipeline
This section covers the scheduling of a set data preparation process in a given dataset.


## TOC
- [Data Description](#data-description)
- [Data Procesing](#data-procesing)
  * [_Requirements_](#-requirements-)
  * [_Scripts_](#-scripts-)
- [Scheduling](#scheduling)
  * [_Running the Scueduler_](#-running-the-scueduler-)
  * [_Expected Output_](#-expected-output-)
  * [_Exiting the Process_](#-exiting-the-process-)
- [Further Study](#further-study)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


<br>

## Data Description
The data  provided in the test repository contains the following columns:
<img src="../misc/data_pipeline_desc.png" alt="pipeline_data_desc" width="300"/>

<br>

## Data Procesing
### _Requirements_
- Split the `name` field into `first_name`, and `last_name`
- Remove any zeros prepended to the `price` field
- Delete any rows which do not have a `name`
- Create a new field named `above_100`, which is `true` if the price is strictly greater than 100

### _Scripts_
The [data preparation script](data_prep) contains functions named by their respective objectives (listed above).

The [cron job script](root) contains the scheduler. 

<br>

## Scheduling
In order to schedule it at a given time interval, a cron job has to be set up.

As containerisation is a major part of cloud processes, which is something I have vested interest in, I decided to take on the challenge to schedule the cron job in a container.

### _Running the Scueduler_
To run the scheduler, run the following command at the [docker directory](docker): `docker build -t cron_job . && docker run --rm -v /path/to/external/volume:/home/data cron_job`.

By default, the cleaned files are saved to `/home/data/cleaned_data`. If you prefer to map it to another path, modify the [scheduler](root) command to the desired path. 

If you are already running the cron job, you can access the container and install vim using `vim /var/spool/cron/crontabs/root` and make the changes to the scheduler or add new jobs.

The [data preparation script](data_prep) accepts two arguments, please check the descriptions in the script. 

<br>

### _Expected Output_
You should see the following output:
```
[Logs regarding cron job actions]
Cleaned /bin/data/raw/dataset1.csv and saved to /home/data/cleaned_data/2022-01-16_01--00_dataset1.csv.
Cleaned /bin/data/raw/dataset2.csv and saved to /home/data/cleaned_data/2022-01-15_12-44-00_dataset2.csv.
```
Note: The example processed files are not processed at the given time as 
### _Exiting the Process_
To exit the docker, open a new console tab or window and find the container ID of the `cron_job` docker.
Run `docker stop <container ID>

<br>

## Further Study
Given the liberty of time, I would like to create a k8 cluster with data persistence such that data cannot be lost easily.