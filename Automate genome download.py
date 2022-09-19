Import os
from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError
Output_directory_pathway = str()
User_input = input(r"Please paste Output directory pathway here: ") + Output_directory_pathway
print(User_input)


for url in [https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/
            "GCF_000001405.39_GRCh38.p13/GCF_000001405.39_GRCh38.p13_assembly_regions.txt",
            https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Balaenoptera_acutorostrata/latest_assembly_versions
            "/GCF_000493695.1_BalAcu1.0/GCF_000493695.1_BalAcu1.0_assembly_report.txt"]:
    # file name append to output_directory
    file_name = os.path.basename(urlparse(url).path)
    print(file_name)
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        with open(os.path.join(User_input, file_name), "wb") as f:
            f.write(response.content)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print("Success")
