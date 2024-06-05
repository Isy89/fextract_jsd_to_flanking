import logging
import pathlib
import pytest

from click.testing import CliRunner
from lbfextract.cli import cli

path_to_tests_folder = pathlib.Path(__file__).parent
path_to_bam = path_to_tests_folder / "test_dataset" / "bam" / "fextract_anonymized_test.bam"
path_to_bed = path_to_tests_folder / "test_dataset" / "multi_bed_ar_ctcf_for_dyads" / "CTCF.sorted.gtrd_version_21_12.1000_sites.hg38.bed"
path_to_bed_dir = path_to_tests_folder / "test_dataset" / "multi_bed_ar_ctcf_for_dyads"
path_to_bam_for_in_batch_tests = path_to_tests_folder / "test_dataset" / "bam" / "fextract_anonymized_test.bam"
path_to_bam_for_dyads = path_to_tests_folder / "test_dataset" / "bam" / "fextract_anonymized_test.bam"
output_path = path_to_tests_folder / "test_out" / "test_cli"

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("fld_type", ["fld", "fld_middle_n"])
def test_extract_jsd_to_flanking(fld_type: str):
    cmd = [
        'feature_extraction_commands',
        ' extract-jsd-to-flanking',
        "--path_to_bam", str(path_to_bam),
        "--path_to_bed", str(path_to_bed),
        "--output_path", str(output_path),
        "--fld_type", fld_type,
    ]
    runner = CliRunner()
    logger.info(f"Testing: extract-jsd-to-flanking with fld_type: {fld_type} ")
    logger.info(" ".join(cmd))
    print(" ".join(cmd))
    result = runner.invoke(cli, " ".join(cmd))
    assert result.exit_code == 0

