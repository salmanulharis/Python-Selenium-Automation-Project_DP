from testrail import *
from datetime import datetime

def get_client():
	client = APIClient('https://zennode.testrail.io/')
	client.user = 'litty@zennode.com'
	client.password = 'QA#INDIAZEN@NELLI'
	return client

def get_project_id(project_name):
	client = get_client()
	projects = client.send_get('get_projects')
	for project in projects['projects']:
		if project['name'] == project_name:
			project_id = project['id']
			#project_found_flag=True
			break
	return project_id

def get_test_run_id(project_name):
	client = get_client()
	project_id = get_project_id(project_name)
	date_and_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
	site_name = 'automation'

	test_run = client.send_post('add_run/%s'%(project_id),{'name': 'test version %s %s'%(date_and_time, site_name)})
	return test_run['id']

def update_test_run(case_id, run_id, result_flag, msg=""):
	client = get_client()
	status_id = 1 if result_flag is True else 5 #status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed

	if run_id is not None:
		try:
			result = client.send_post('add_result_for_case/%s/%s'%(run_id,case_id),{'status_id': status_id, 'comment': msg })
		except Exception as e:
			print('Exception in update_testrail() updating TestRail.')
			print('PYTHON SAYS: ')
			print(e)
		else:
			print('Updated test result for case: %s in test run: %s with msg:%s'%(case_id,run_id,msg))

# update_test_run(1010977, 9909, True, "The test run is completed")