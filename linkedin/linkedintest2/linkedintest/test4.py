from bs4 import BeautifulSoup
html1="""<section id="experience-section" class="pv-profile-section experience-section ember-view"><header class="pv-profile-section__card-header">
  <h2 class="pv-profile-section__card-heading">
    Experience
  </h2>

<!----></header>

  <ul class="pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more">
<li id="ember328" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="ember330" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
<a data-control-name="background_details_company" href="/company/ibm/" id="ember331" class="full-width ember-view">        <div class="pv-entity__company-details">
  <div class="pv-entity__logo company-logo">
    <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGfKOtAsJ7gOQ/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=luGBb3MHs2C8l7XD2oVMdLydU8-rI-qie4urmsYipEE" loading="lazy" alt="IBM India Private Limited" id="ember333" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
  </div>
  <div class="pv-entity__company-summary-info">
    <h3 class="t-16 t-black t-bold">
      <span class="visually-hidden">Company Name</span>
      <span>IBM India Private Limited</span>
    </h3>
        <h4 class="t-14 t-black t-normal">
          <span class="visually-hidden">Total Duration</span>
          <span>2 yrs</span>
        </h4>
  </div>
</div>
</a>
<!---->  </div>

    <ul class="pv-entity__position-group mt2">
        <li class="pv-entity__position-group-role-item">
          <div id="ember335" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container pv-entity__role-details-container--timeline pv-entity__role-details-container--bottom-margin">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>Managing Consultant</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>Jan 2017</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">less than a year</span>
                </h4>
            </div>

            <h4 class="pv-entity__location t-14 t-black--light t-normal block">
              <span class="visually-hidden">Location</span>
              <span>Kolkata Area, India</span>
            </h4>
<!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
        <li class="pv-entity__position-group-role-item">
          <div id="ember337" class="ember-view"><div class="pv-entity__role-details">
  <span class="pv-entity__timeline-node"></span>
  <div class="display-flex justify-space-between full-width">
    <div class="pv-entity__role-container">
      <div class="pv-entity__role-details-container  ">

        <div class="pv-entity__summary-info-v2 pv-entity__summary-info--background-section pv-entity__summary-info-margin-top ">
          <h3 class="t-14 t-black t-bold">
            <span class="visually-hidden">Title</span>
            <span>Senior System Analyst</span>
          </h3>
<!---->            <div class="display-flex">
              <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
                <span class="visually-hidden">Dates Employed</span>
                <span>Oct 2015 – Dec 2016</span>
              </h4>
                <h4 class="t-14 t-black--light t-normal">
                  <span class="visually-hidden">Employment Duration</span>
                  <span class="pv-entity__bullet-item-v2">1 yr 3 mos</span>
                </h4>
            </div>

            <h4 class="pv-entity__location t-14 t-black--light t-normal block">
              <span class="visually-hidden">Location</span>
              <span>Kolkata Area, India</span>
            </h4>
<!---->        </div>


<!---->      </div>
    </div>

<!---->  </div>
</div>
</div>
        </li>
    </ul>

<!----></section>
</li><li id="ember339" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="503098743" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/search/results/all/?keywords=Wipro" id="ember342" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Wipro" id="ember344" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ghost-company ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Architect</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Wipro
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Dec 2013 – Oct 2015</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 11 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li><li id="ember347" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="473904771" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/ibm/" id="ember350" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGfKOtAsJ7gOQ/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=luGBb3MHs2C8l7XD2oVMdLydU8-rI-qie4urmsYipEE" loading="lazy" alt="IBM" id="ember352" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Senior System Analyst</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      IBM
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Feb 2006 – Dec 2013</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">7 yrs 11 mos</span>
      </h4>
  </div>

  <h4 class="pv-entity__location t-14 t-black--light t-normal block">
    <span class="visually-hidden">Location</span>
    <span>Kolkata Area, India</span>
  </h4>

<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li><li id="ember355" class="pv-entity__position-group-pager pv-profile-section__list-item ember-view">        <section id="159482264" class="pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view">  <div class="display-flex justify-space-between full-width">
    <div class="display-flex flex-column full-width">
<a data-control-name="background_details_company" href="/company/infosys/" id="ember358" class="full-width ember-view">          <div class="pv-entity__logo company-logo">
  <img src="https://media-exp1.licdn.com/dms/image/C4E0BAQGcC5nkmHu2cg/company-logo_100_100/0?e=1599091200&amp;v=beta&amp;t=rPRqwVCgBeGTI2sOrctd8Vy6bh_Iv3aCrwmNEZfWveA" loading="lazy" alt="Infosys Technologies Ltd" id="ember360" class="pv-entity__logo-img EntityPhoto-square-5 lazy-image ember-view">
</div>
<div class="pv-entity__summary-info pv-entity__summary-info--background-section ">
  <h3 class="t-16 t-black t-bold">Software Engineer</h3>
  <p class="visually-hidden">Company Name</p>
  <p class="pv-entity__secondary-title t-14 t-black t-normal">
      Infosys Technologies Ltd
<!---->  </p>
    <div class="display-flex">
    <h4 class="pv-entity__date-range t-14 t-black--light t-normal">
      <span class="visually-hidden">Dates Employed</span>
      <span>Sep 2004 – Feb 2006</span>
    </h4>
      <h4 class="t-14 t-black--light t-normal">
        <span class="visually-hidden">Employment Duration</span>
        <span class="pv-entity__bullet-item-v2">1 yr 6 mos</span>
      </h4>
  </div>

<!---->
<!---->
</div>

</a>
<!---->    </div>

<!---->  </div>
</section>
</li>  </ul>

<!----></section>
"""
# test=.find("div",{"class":"blended-srp-results-js pt0 pb4 ph0 container-with-shadow"}).find("h3")	  
# expsect=BeautifulSoup(html1,'html.parser').find("section", {"id":"experience-section"})
exp=BeautifulSoup(html1,'html.parser').find_all("div", {"class":""})
print(exp)
# for k in BeautifulSoup(html1,'html.parser').find_all("section",{"pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"}):
#         designation=k.find("h3",{"class":"t-16 t-black t-bold"})
#         # print(designation.text)
#         company=k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"})
#         # if company is not None:
#         print(company)
#         dates_employed=k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"})
#         # if company is not None:
#         # print(dates_employed.txt)
#         #dates_employed1=dates_employed.find("span",{"class":"visually-hidden"})
#         employ_duration=k.find("span",{"class":"pv-entity__bullet-item-v2"})
#         # if employ_duration is not None:
#         # print(employ_duration)
j=0
while(j<len(exp)):
        k=exp[j]  
        designation=k.find("h3",{"class":"t-16 t-black t-bold"})
        print(designation.text)
        company=k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"})
        print(company.text)
        dates_employed=k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"})
        print(dates_employed)
        #dates_employed1=dates_employed.find("span",{"class":"visually-hidden"})
        employ_duration=k.find("span",{"class":"pv-entity__bullet-item-v2"})
        print(employ_duration)
        # expdict[j]={'id':j,'designation': designation.text, 'company': company.text.strip(),'employ_duration':employ_duration.text}
        j=j+1
