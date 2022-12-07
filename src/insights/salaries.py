from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    all_values = [
        job["max_salary"]
        for job in data
        if (job["max_salary"]).isdigit()]
    value_max = max([int(value) for value in all_values])
    return value_max
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    all_values = [
        job["min_salary"]
        for job in data
        if (job["min_salary"]).isdigit()]
    value_min = min([int(value) for value in all_values])
    return value_min
    # raise NotImplementedError


def check_min_and_max_salay_in_job(job: Dict) -> bool:
    """ Check if min_salary and max_salary is int or srt and is digit
      and check if min_salary < max_salary """
    if (
        "min_salary" not in job or "max_salary" not in job
        or not isinstance(job["min_salary"], (str, int))
        or not isinstance(job["max_salary"], (str, int))
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError

    return True


def check_salay_is_valid(salary: Union[int, str]) -> bool:
    """Check if salary is int or srt and str is digit"""
    if (
        not isinstance(salary, (str, int))
        or isinstance(salary, str) and not salary.isdigit()
    ):
        raise ValueError

    return True


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    check_min_and_max_salay_in_job(job)
    check_salay_is_valid(salary)

    result = int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    return result
    # raise NotImplementedError


def catch(job: Dict, salary: Union[str, int]):
    """
https://stackoverflow.com/questions/1528237/how-to-handle-exceptions-in-a-list-comprehensions
    expesifica for this application
    but I looked for the idea of this solution in the stack overflow
    of how to do a list comprehension with try except
    """
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        pass


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    result = [job for job in jobs if catch(job, salary)]
    return result
    #    * result = list()
    #    * for job in jobs:
    #    *     try:
    #    *         if (matches_salary_range(job, salary)):
    #    *             result.append(job)
    #    *     except ValueError:
    #    *         pass
    #    * return result
    # raise NotImplementedError
